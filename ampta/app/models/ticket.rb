class Ticket < ActiveRecord::Base
  attr_accessible :name, :description, :start_date, :end_date, :status_id, :project_id
  belongs_to :user
  belongs_to :project
  belongs_to :status

  validates :name,
            :presence => true,
            :length => { :in => 3..30, :allow_blank => true }

  validates_presence_of :description, :start_date, :end_date

end
