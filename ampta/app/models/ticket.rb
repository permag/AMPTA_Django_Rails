class Ticket < ActiveRecord::Base
  attr_accessible :name, :description, :start_date, :end_date, :status_id, :project_id
  belongs_to :user
  belongs_to :project
  belongs_to :status

  validates_presence_of :name, :description, :start_date, :end_date

  validates :name,
            :length => { :minimum => 3, :maximum => 30 }

end
