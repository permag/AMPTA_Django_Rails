class Ticket < ActiveRecord::Base
  attr_accessible :name, :description, :start_date, :end_date, :status_id, :project_id
  belongs_to :user
  belongs_to :project
  belongs_to :status

  validates :name,
            :presence => true,
            :length => { :in => 3..30, :allow_blank => true }

  validates_presence_of :description, :start_date, :end_date

  validate :validate_end_date_before_start_date

  def validate_end_date_before_start_date
    if end_date && start_date
      errors.add(:end_date, "must be greater than start date.") if end_date <= start_date
    end
  end

end
